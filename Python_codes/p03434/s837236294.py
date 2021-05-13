N = int(input())
A = list(map(int, input().split()))

alice = 0
bob = 0

A_rev = sorted(A, reverse=True)

while True:
    if len(A_rev) != 0:
        alice += A_rev.pop(0)
    
    if len(A_rev) != 0:
        bob += A_rev.pop(0)
    
    if len(A_rev) == 0:
       break
 
print(alice - bob)