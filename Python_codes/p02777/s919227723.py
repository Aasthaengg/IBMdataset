#!/usr/bin/env python3
(s,t,),(a,b,),(u,)=[t.split() for t in open(0)]
print(int(a)-(s==u),int(b)-(t==u))
