n, k = map(int, input().split())
AA =[int(a) for a in input().split()]


for b, t in zip(AA, AA[k:]):
    if t > b:
        print("Yes")
    else:
        print("No")
