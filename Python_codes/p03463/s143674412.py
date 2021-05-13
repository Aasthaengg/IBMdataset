#template
def inputlist(): return [int(j) for j in input().split()]
#template
#issueから始める
N,A,B = inputlist()
if (B-A-1) % 2 == 1:
    print("Alice")
if (B-A-1) % 2 == 0:
    print("Borys")