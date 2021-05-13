A,B,K = (int(x) for x in input().split())
if A+B<K:
    print('0 0')
elif A<K<=A+B:
    print('0 {}'.format(A+B-K))
elif 0<=K<=A:
    print('{} {}'.format(A-K,B))