# solution
import io
import math

nim = int(input())
mike = int(input())
counter = 1
for i in range(nim):
    if counter < mike:
        counter*=2
    else:
        counter+=mike
print(counter)