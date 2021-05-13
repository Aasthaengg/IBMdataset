X, A, B = map(int, input().split())
print(["delicious","safe","dangerous"][(B-A>=X+1)+(B-A>0)])