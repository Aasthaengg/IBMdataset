from sys import stdin
def main():
    #入力
    readline=stdin.readline
    s=readline().strip()
    
    if s=="Sunny":
        print("Cloudy")
    elif s=="Cloudy":
        print("Rainy")
    else:
        print("Sunny")
        
if __name__=="__main__":
    main()