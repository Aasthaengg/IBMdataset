"""Boot-camp-for-Beginners_Easy011_B_Collatz-Problem_29-August-2020.py"""
import numpy as np

#N = 100
N=int(input())
Division_2 = []
number=[]
for i in range(1, N+1):
    j = i
    count = 0
    while True:
        if j/2 != int(j/2):
            break
        j = j/2
        count += 1
    Division_2.append(count)
    number.append(i)
Division_2=np.array(Division_2)
print(number[np.argmax(Division_2)])
#print(Division_2)
