s = input()
w = int(input())
ans = [ s[i] for i in range(0, len(s),w)]
print("".join(ans))