"""Boot-camp-for-Beginners_Easy004_B_Tax-Rate_25-August-2020.py"""
import numpy as np
import sys

N=int(input())
X=N/1.08
if int(int(np.ceil(X))*1.08)==N:
    print(int(np.ceil(X)))
else:
    print(":(")