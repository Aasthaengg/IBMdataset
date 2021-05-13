import numpy as np
def main():
    n = int(input())
    count = np.zeros((10, 10))
    for i in range(1, n + 1):
        i = str(i)
        s = int(i[0])
        e = int(i[-1])
        count[s, e] += 1
    print(np.sum(count * count.T, dtype = np.int))

if __name__ == '__main__':
    main()
