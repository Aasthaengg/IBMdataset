"""Boot-camp-for-Beginners_Easy008_B_1-21_28-August-2020.py"""
import numpy as np

a, b = map(int, input().split())

AB = int(str(a) + str(b))
if np.sqrt(AB)==int(np.sqrt(AB)):
    print("Yes")
else:
    print("No")
