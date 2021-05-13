N = int(input())

i = N//100
j = (N - 100*i)//10
k = (N - 100*i - 10*j)

print("Yes" if i == k else "No")