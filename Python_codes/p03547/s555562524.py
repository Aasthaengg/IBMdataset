# -*- coding: utf-8 -*-
X, Y = map(str, input().split())

print('<' if X < Y else '>' if X > Y else '=')