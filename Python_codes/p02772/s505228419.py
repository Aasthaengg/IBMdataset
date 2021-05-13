N = int(input())
N_List = list(map(int,input().split()))

X = [x for x in N_List if x % 2 ==0]
Y = [y for y in X if y % 3 ==0 or y % 5 ==0]

if len(X) == len(Y):
    print("APPROVED")
else:
    print("DENIED")