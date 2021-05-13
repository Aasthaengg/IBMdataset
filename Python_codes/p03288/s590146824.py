import numpy

def judge(r):
    if r < 1200:
        print("ABC")
    elif (1200 <= r) & (r < 2800):
        print("ARC")
    elif 2800 <= r:
        print("AGC")

if __name__ == "__main__":
    r = int(input())
    judge(r)
