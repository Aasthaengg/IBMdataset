# import matplotlib.pyplot as plt
import math

def squaredDistance(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

# for X in range(1, 180):
angle = 90
X = int(input())
iter = 0
current = [0, 0]
previous = current

while (iter == 0 or squaredDistance(current, [0, 0]) > 0.00001):
  if (iter > 500):
    break

  dir = [math.cos(math.radians(angle)), math.sin(math.radians(angle))]
  current = [current[0] + dir[0], current[1] + dir[1]]
  angle = (angle + X) % 360
  # plt.plot([previous[0], current[0]], [previous[1], current[1]])
  previous = current
  iter = iter + 1

  # plt.show()

print(iter)
  # print("X = {} : {}".format(X, iter))

