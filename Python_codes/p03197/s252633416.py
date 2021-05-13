N = int(input())
l = [int(input()) for _ in range(N)]
print("second" if all(map(lambda x:x%2==0, l)) else "first")