import sys


def read_data():
    r_data = []
    n = int(sys.stdin.readline().strip())
    
    for _ in range(n):
        r = int(sys.stdin.readline().strip())
        r_data.append(r)

    return n, r_data
    
def main():
    n, r_data = read_data()
    maxv = -1000000000
    minv = r_data[0]
    
    for j in range(1, n):
        if r_data[j] - minv > maxv:
            maxv = r_data[j] - minv

        if r_data[j] < minv:
            minv = r_data[j]

    print(maxv)

if __name__ == '__main__':
    main()