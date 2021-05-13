s = input()
w = int(input())
ans = [s[i] if i % w == 0 else "" for i in range(len(s))]
print("".join(ans))