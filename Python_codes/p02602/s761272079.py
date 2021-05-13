sem, per = map(int, input().split())
scores = list(map(int, input().split()))

for i in range(sem - per):
    if scores[i] < scores[i + per] :
        print('Yes')
    else:
        print('No')