l=list(map(int,input().split()))
gedoku_not=l[0]
gedoku_good=l[1]
poison=l[2]
ans=0
if poison<=gedoku_good+gedoku_not:
    print(poison+gedoku_good)
else:
    print(gedoku_good*2+gedoku_not+1)