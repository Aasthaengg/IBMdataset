def main():
    r, D, x = map(int, input().split())
    t = x
    for i in range(10):
        t = (r*t)-D
        print(t)
main()  
