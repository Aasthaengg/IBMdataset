import math
  
def floatinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = float(a[i])
    return a
     
def main():
    a = floatinput()
    x1 = a[0]; y1 = a[1]; x2 = a[2]; y2 = a[3]
    print(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
     
if __name__ == "__main__":
    main()
