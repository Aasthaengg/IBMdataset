N = int(input())
s = input()[::-1]
T = list(input()[::-1])

index = len(T)
for i, t in enumerate(T):
    if t == s[0]:
        j = 0
        while j < len(T) - i:
            if s[j] != T[i + j]:
                break
            j += 1
        else:
            index = i
            break

res = s[::-1] + "".join((T[:index])[::-1])
print(len(res))
