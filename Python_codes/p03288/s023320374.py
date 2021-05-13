r = int(input()) 
def contest(rate):
    if rate<1200:
        return "ABC"
    elif 1200<=rate<2800:
        return "ARC"
    else:
        return "AGC"
print(contest(r))
