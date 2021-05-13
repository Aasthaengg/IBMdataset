def resolve():
    import math
    from functools import reduce
    
    def lcm_base(x, y):
        return (x * y) // math.gcd(x, y)
      
    def lcm_list(numbers):
        return reduce(lcm_base, numbers, 1)
    
    n = int(input())
    A = list(map(int, input().split()))
    lcm = lcm_list(A)
    m = lcm-1
    ans = 0
    for i in range(n):
      ans += m % A[i]
    print(ans)
resolve()