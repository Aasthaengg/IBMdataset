import math
if __name__ == "__main__":
    r = float(input())
    equivalent_of_circle = math.pi*(r**2)
    len_of_circle = math.pi*r*2
    print("%0.6f %0.6f"%(equivalent_of_circle,len_of_circle))