n = input()
m = [int(n[i:i+3]) for i in range(len(n)-2)]
ans = [abs(753 - j) for j in m]
print(min(ans))