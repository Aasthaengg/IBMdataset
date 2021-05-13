n, a, b = map(int,input().split())
print((n // (a + b)) * a + ( n % (a + b) ) % a if (n % (a + b) ) < a else (n // (a + b)) * a + a)