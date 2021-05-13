#!/usr/bin/env python3

d, n = map(int,input().split())
ans = n*(n-1)**(d-1)
print(ans)
