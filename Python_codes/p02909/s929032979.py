def resolve():
    S = input()
    d = {
        "Sunny": "Cloudy",
        "Cloudy": "Rainy",
        "Rainy": "Sunny"
    }
    print(d[S])
    
if '__main__' == __name__:
    resolve()