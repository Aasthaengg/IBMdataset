# -*- coding: utf-8 -*-
ab, bc, ca = map(int,input().split()) 

ans = ab * bc * ca // max(ab, bc, ca)
print(ans // 2)
