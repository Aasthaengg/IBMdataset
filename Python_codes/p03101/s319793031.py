import os, sys, re, math

(H, W) = [int(n) for n in input().split()]
(h, w) = [int(n) for n in input().split()]

print(H * W - (h * W + H * w - h * w))
