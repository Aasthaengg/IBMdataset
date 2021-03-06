"""
最大限傾けたとき、水と接している面は横から見ると台形ないし三角形となる
水と接している面の面積 x/a が a*b/2 より大きい場合は台形となり、以下の場合は三角形となる

台形の場合

最大限傾けたとき、水と接している台形の上辺の長さをnとすると
(n+b)*a/2 = x/a
n = 2*x/(a**2) - b
求める角度をthetaとすると
tan(theta) = (b-n)/a
theta = arctan((b-n)/a)

三角形の場合

最大限傾けたとき、水と接している三角形の底辺の長さをnとすると
n*b/2 = x/a
n = 2*x/(a*b)
求める角度をthetaとすると
tan(theta) = b/n
theta = arctan(b/n)
"""

import sys
sys.setrecursionlimit(10**6)

a,b,x = map(int, input().split())

import numpy as np

if x/a > a*b/2:
    n = 2*x/(a**2) - b
    theta = np.arctan((b-n)/a) # radian表記なので戻り値の範囲は[-pi/2, pi/2]
    theta = np.rad2deg(theta)
else:
    n = 2*x/(a*b)
    theta = np.arctan(b/n)
    theta = np.rad2deg(theta)

print(theta)