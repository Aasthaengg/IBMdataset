
import itertools

def main():
    
    input_lines_n = input()
    n = int(input_lines_n)
    xyz_max = 100
    l = [0] * 10001
    
    for x, y, z in itertools.product(range(xyz_max), range(xyz_max), range(xyz_max)):
        fn = 0
        if x > 0 and y > 0 and z > 0:
            fn = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if fn <= n:
                l[fn] += 1
    
    for i in range(1, n+1):
        print(l[i])
                    
    
if __name__ == "__main__":
    main()
