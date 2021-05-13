#!/usr/bin/env python3
(*t, ) = map(int, open(0).read().split())
print(sum(-(-i // 10)*10 for i in t) + min(-(-i % 10) for i in t))
