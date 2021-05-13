def smaller(a, b):
    n = min(len(a), len(b))
    for i in reversed(range(n)):
        if a[i] < b[i]:
            return True
        elif b[i] < a[i]:
            return False
    return len(a) < len(b)
    
  
    

a, b = [int(x) for x in raw_input().split()]

a_r = ''.join([str(a) for _ in range(b)])

b_r = ''.join([str(b) for _ in range(a)])

if smaller(a_r, b_r):
    print(a_r)
else:
    print(b_r)





