A,B,K = (int(x) for x in input().split())
print('{} {}'.format(max(0,A-K),max((0<=K<=A)*B,(A<K)*max(A+B-K,0))))