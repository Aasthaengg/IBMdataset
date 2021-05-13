import numpy as np

N = int(input())
T, A = map(int,input().split())
H = np.array(list(map(int,input().split())))

temperatures = list(abs([T]*N - H*0.006 - [A]*N))

print(temperatures.index(min(temperatures))+1)
