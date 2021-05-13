def main():
    S = input()
    ans = "AKIHABARA"
    ls1 = ["AKIHABARA","KIHABARA","AKIHBARA","AKIHABRA","AKIHABAR"]
    ls2 = ["KIHBARA","KIHABRA","KIHABAR","AKIHBRA","AKIHBAR","AKIHABR"]
    ls3 = ["KIHBRA","KIHABR","KIHBAR","AKIHBR"]
    ls4 = ["KIHBR"]
    ls = ls1+ls2+ls3+ls4

    if S in ls:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()