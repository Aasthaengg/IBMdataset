import collections
N, K = map(int, input().split())
l = list(map(int, input().split()))

if len(list(set(l))) <= K:
    print(0)
else:
    result = 0
    
    ii =  len(list(set(l))) - K

    c = collections.Counter(l)
    l_r = c.most_common()
    for i in range(ii):
        c = i+1
        
        result += l_r[-1*c][1]
        
    print(result)
        
