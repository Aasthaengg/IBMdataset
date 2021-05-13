#template
def inputlist(): return [int(j) for j in input().split()]
#template
#issueから始める
A,B,C,K = inputlist()
if abs(B-A) >= 10**18:
    print("Unfair")
    exit()
ans = A-B
if K % 2 == 1:
    ans *= -1
print(ans)