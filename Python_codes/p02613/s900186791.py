
def main():
    N = int(input())
    d = {"AC":0, "WA":0, "TLE":0, "RE":0}
    for i in range(N):
        d[input()] +=1
    for key, value in d.items():
        print(f"{key} x {value}")
        

if __name__ == "__main__":
    main()