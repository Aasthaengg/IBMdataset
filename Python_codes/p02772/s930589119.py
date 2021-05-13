N = int(input())
A = list(map(int, input().split()))
even = [i for i in A if i % 2 == 0]

if all([i % 3 == 0 or i % 5 == 0 for i in even]) == True:
    print("APPROVED")
else:
    print("DENIED")