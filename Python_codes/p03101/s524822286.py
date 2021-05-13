# -*- coding: utf-8 -*-
import math
import datetime

# 入力
#N = int(input())
#S = str(input())
H, W = map(int, input().split())
hi, wi = map(int, input().split())

print ((H*W) - ((hi*W) + (wi*H) - (hi*wi)))