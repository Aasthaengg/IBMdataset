N = int(input())
A = list(map(int, input().split()))
print("APPROVED" if all(a&1 or (a%3==0 or a%5==0) for a in A) else "DENIED")