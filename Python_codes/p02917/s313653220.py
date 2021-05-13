N = int(input())
B = list(map(int, input().split()))
B = [10**5] + B + [10**5]
print(sum(min(B[i], B[i+1]) for i in range(N)))