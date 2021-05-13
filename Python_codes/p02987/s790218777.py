
def main():
    s = input()
    s_ = list(set(s))
    if s.count(s_[0]) == 2 and len(s_) == 2:
        print('Yes')
    else:
        print('No')
   

if __name__ == "__main__":
    main()
