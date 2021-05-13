lngs = input()

ACGT = ["A", "C", "G", "T"]
out_list = []
out_list_long = []


for lng in lngs:

    if lng in ACGT:
        out_list += lng
    else:
        if len(out_list) > len(out_list_long):
            out_list_long = []
            out_list_long = out_list
        out_list = []

if len(out_list) > len(out_list_long):
    out_list_long = []
    out_list_long = out_list

print(len(out_list_long))
