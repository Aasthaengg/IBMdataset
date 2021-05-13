N = int(input())
A = int(input())
buf =N - ((N//500)*500)
print("Yes" if A >= buf else "No")