N = int(input())
A = input()
w = [A[0] == "W"]
for i in range(1, N):  w.append(w[-1] + (A[i] == "W"))
e = [A[0] == "E"]
for i in range(1, N):  e.append(e[-1] + (A[i] == "E"))
ans = min(e[-1] - e[0], w[-2])
for i in range(1, N - 1):  ans = min(ans, w[i - 1] + e[-1] - e[i])
print(ans)