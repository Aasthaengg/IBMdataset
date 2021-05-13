# -*- coding: utf-8 -*-
from math import pi

r = float(input())
area = r**2*pi
circumference = r*pi*2
              
print("{:.6f} {:.6f}".format(area, circumference))